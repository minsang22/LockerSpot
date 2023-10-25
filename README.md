**HW #5** 

The Final Project with Object-Oriented ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.001.png)

Analysis and Designs 

소속 : 소프트웨어융합대학 소프트웨어학부 학번 : 20191610, 20191631 

이름 : 성정규, 윤민상 

1. **Project Team** 정하기** 
**
` `인원** 수 **: 2**명** 

` `이름 : 윤민상 

` `학번 : 20191631 

` `전공 : 소프트웨어전공 

` `업무 경험 : Python, C++을 활용한 휴머노이드 로봇 대회에 여러번 참여하며 컴퓨터비전(영상처리) 

` `프로젝트 경험, 2020년도 동계 인턴에서 React Native를 사용한 모바일 앱 프론트엔드 개발 경험, 2020년도 동계 인턴에서 무인 음주측정기 제작 프로젝트에 참여해 Python을 사용한 사람 얼굴/입 추적  프로그램 개발 경험 

` `강점 소개 : 휴머노이드 로봇으로 주어진 미션을 수행하는 여러 대회에 참여했었고, 그 과정에서 영상처리  파트를 맡은 경험이 있어 OpenCV를 사용한 개발을 할 수 있습니다. 그 중에서도 물체를 추적하거나 

` `라벨링하고, 물체를 인식하는 분야의 기능 개발에 강점이 있습니다. ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.002.png)

` `이름 : 성정규 

` `학번 : 20191610 

` `전공 : 소프트웨어전공 

` `업무 경험 : Python, C++을 활용한 간단한 프로젝트 경험, 안드로이드 스튜디오와 Kotlin 활용한 앱  프로젝트 프론트엔드 개발 경험, Flutter을 활용한 앱 프로젝트 프론트엔드 개발 경험이 있습니다. 

` `강점 소개 : 앱 개발 프로젝트에서 디자인 및 프론트엔드 기능 개발을 맡은 경험이 있어 사용자 측면에서 UI/UX 디자인을 할 수 있습니다. 또한 그 디자인을 퍼블리싱하고 기능 개발을 할 줄 알고 있습니다. 

2. 관심이** 있던 **Project** 내용** 

**2-1.** 사물함** 신청** 및** 관리** 시스템** 
**
` `목적** 

- 매 학기 학생회에서 받는 사물함 신청 과정의 간편화 
- 사물함을 신청하는 학생들의 편리성 증가 
- 사물함 반납 기능을 통한 좀 더 유동적인 사물함 사용 
**
` `개발 **: Python (PyQt** 활용**), Firebase**를** 통한 **DB** 관리** 
**
` `핵심** 기능** 

- 학생 로그인 : 학생들이 학번과 비밀번호를 입력하여 로그인할 수 있습니다. 
- 사물함 신청 : 각 학생이 원하는 사물함을 신청할 수 있습니다. 여러 개의 사물함 중 선택  가능하며, 선택한 사물함의 위치와 번호가 보여집니다. 
- 사물함 반납 : 각자 사용중인 사물함을 반납할 수 있습니다. 
- 사물함 이용 내역 확인 : 각 학생은 자신이 사용한 사물함의 이용 내역을 확인할 수 있습니다. 이용  내역에는 사용 기간, 남은 기간, 사용일 등이 포함됩니다. 
- 관리자 로그인 : 관리자는 관리자 계정으로 로그인할 수 있습니다. 
- 사물함 목록 확인 : 관리자는 현재 사용중인 사물함 목록과 사용 가능한 사물함 목록을 확인할 수  있습니다. 또한, 선택한 사물함의 이용 내역도 확인할 수 있습니다. 
- 사물함 할당 및 반납 : 관리자는 사용 가능한 사물함을 학생에게 할당하거나, 사용 중인 사물함을  반납받을 수 있습니다. 
- 학생 목록 확인 : 관리자는 현재 등록된 학생 목록을 확인할 수 있습니다. 학생 목록에는 학번, 

` `이름, 학과, 전화번호 등의 정보가 포함됩니다. 
**
` `사용자** 측면 **UI** 

- 로그인 화면 : 학생과 관리자 각각의 로그인 화면이 있습니다. 로그인 화면에서는 학번과  비밀번호를 입력합니다. 
- 메인 화면 : 학생과 관리자 각각의 메인 화면이 있습니다. 학생은 사물함 신청 및 반납, 이용 내역  확인을 할 수 있습니다. 관리자는 사물함 목록 확인, 사물함 할당 및 반납, 학생 목록 확인을 할 수  있습니다. 
- 사물함 신청 화면 : 학생이 사물함을 신청할 수 있는 화면입니다. 여러 개의 사물함 중 선택  가능하며, 선택한 사물함의 위치와 번호가 보여집니다. 
- 이용 내역 화면 : 학생이 자신의 사물함 이용 내역을 확인할 수 있는 화면입니다. 이용 내역에는 

` `사용 기간, 남은 기간, 사용일 등이 포함됩니다. 

**2-2.** 동네인증** 커뮤니티** 
**
` `목적** 

- 지역 주민들끼리 소통하고 정보를 공유하는 모바일 플랫폼 제공 
- 지역 주민들의 교류와 화합의 장 
**
` `개발 **: Kotlin**을** 통한** 개발**, Firebase**를** 통한 **DB**관리**  핵심** 기능** 

- 지도 API를 이용하여 지역인증 후 지역 주민들끼리의 소통 공간 제공 
- 글쓰기 기능 
- 댓글 작성 기능 
- 사진 업로드 기능 
**
` `사용자** 측면** 

- 로그인 : 카카오톡 등 SNS 계정을 이용한 간편 로그인, 이메일 로그인 제공 
- 사용자 프로필 : 사용자 정보를 등록하고 관리할 수 있도록 제공 
- 글쓰기 : 제목, 내용, 사진 등을 업로드할 수 있으며, 카테고리별로 분류할 수 있도록 제공 
- 댓글 작성 : 사용자들간의 소통을 위해 댓글 작성 기능 제공 
- 검색 기능 : 사용자가 필요한 정보를 검색할 수 있도록 검색 기능 제공 
- 지역 인증 : 지도 API를 활용하여 사용자의 위치를 확인하고, 지역구 단위로 플랫폼을 이용할 수  있게 함 
1. 프로젝트** 주제** 
1. 프로젝트명 

Locker Spot 

2. 프로젝트 내용 

` `현재 매 학기 학생회에서 사물함 신청을 받고, 이를 학생들에게 배분해주는 방식으로 사물함을 사용하고  있습니다. 이 때 사용할만한 마땅한 방법이 없어 신청하는 학생들과, 신청을 받아 사물함을 배분해주는  학생회 인원들 모두가 불편함을 겪고 있습니다. 이 과정에서 사용할 수 있는 프로그램을 만들어 사물함  신청 과정을 간편화하고, 사물함을 신청하는 학생들의 편리성을 증가시킬 예정입니다. 또한 현재 한번 

` `신청한 사물함을 한 학기동안 사용하는데, 모든 학생들이 듣는 과목과 개인 일정이 다르다보니 사용하지  않고 비어있는 사물함이 존재합니다. 이 문제를 해결하기 위해 프로그램에 사물함 반납 기능을 추가하여  좀 더 유동적으로 사물함을 사용할 수 있도록 하고 싶습니다. 

3. 프로젝트의 범위 

` `프로젝트의 목적은 소프트웨어융합대학 모든 학생이 사용할 수 있게 하는 것이기에 기능적인 요구사항과  비기능적인 요구사항 등 분석 및 설계는 그정도의 규모로 예상하고 진행할 예정입니다. 

` `분석 및 설계 단계에서는 시스템의 요구사항을 분석하고, 사용자의 요구사항에 맞게 설계를 진행할 

` `예정입니다. 구현 단계에서는 Python 언어와 PyQt를 사용하여 사용자 인터페이스 및 기능을 구현하고, Firebase를 이용하여 데이터베이스 관리를 할 예정입니다. 현재는 모든 재학생이 사용할 수 있을 정도의  규모로 서버를 열고 유지하는 데에 어려움이 있기 때문에 서버를 열지 않고 local 환경에서 개발 및 실행  가능하도록 개발을 진행할 예정이며, 이후에 서버 관리 및 유지보수에 대해서는 별도로 검토하여 결정할  예정입니다. ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.003.png)

2. 기능적** 요구사항** 도출** 
1. Use Case Model 도출 



|**Use Case** |**Actor** |** 설명** |
| - | - | - |
|` `학생 로그인 |` `학생 |` `학생이 학번과 비밀번호를 입력하여 로그인한다. |
|` `사물함 신청 |` `학생 |` `학생이 원하는 사물함을 신청한다. |
|` `사물함 반납 |` `학생 |` `학생이 사용 중인 사물함을 반납한다. |
|` `이용 내역 확인 |` `학생 |` `학생이 자신이 사용한 사물함의 이용 내역을 확인한다. |
|` `관리자 로그인 |` `관리자 |` `관리자가 관리자 계정으로 로그인한다. |
|` `사물함 목록 확인 |` `관리자 |` `관리자가 현재 사용중인 사물함 목록과 사용 가능한 사물함 목록을  확인한다. |
|` `사물함 할당 및  반납 |` `관리자 |` `관리자가 사용 가능한 사물함을 학생에게 할당하거나, 사용 중인 사물함을  반납받는다. |
|` `학생 목록 확인 |` `관리자 |` `관리자가 현재 등록된 학생 목록을 확인한다. |

2. Use Case Description 작성 Use Case 1 : 학생 로그인 



<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `학생 로그인 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `학생이 학번과 비밀번호를 입력하여 로그인한다. </td></tr>
<tr><td colspan="1"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `학생이 로그인을 시도한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `학생이 학번과 비밀번호를 입력하여 시스템에 로그인한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `학생 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `사물함 신청 / 사물함 반납 </td></tr>
<tr><td colspan="1"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자(학생회) </td></tr>
<tr><td colspan="1"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `학생은 학번과 비밀번호가 시스템에 등록되어 있어야 한다. </td></tr>
<tr><td colspan="1"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `학생은 시스템에 로그인되어 있다. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1"><p>1. 로그인 페이지에 접속한다. </p><p>2. 학번과 비밀번호를 입력한다. </p><p>3. 로그인 버튼을 클릭한다. </p></td><td colspan="1"><p>1\.1. 로그인 페이지를 보여준다. </p><p>2\.1. 입력된 학번과 비밀번호를 </p><p>` `확인한다. </p><p>3\.1. 해당 학생 계정으로 로그인시킨다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top"><p>2\.1. 학번이나 비밀번호를 잘못 입력한 경우: 입력한 정보가 시스템에 등록되어  있는 정보와 일치하지 않으면 로그인이 실패한다. </p><p>2\.1. 시스템에 등록되지 않은 학번인 경우: 입력한 학번이 시스템에 등록되어 </p><p>` `있지 않으면 로그인이 실패한다. </p></td></tr>
</table>

Use Case 2 : 사물함 신청 
<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `사물함 신청 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `학생이 원하는 사물함을 신청한다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `학생이 사물함을 신청하고자 한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `학생이 사용할 수 있는 사물함을 확인하고 사물함 신청을 위해 시스템에  요청하고, 해당 사물함을 사용할 수 있게 된다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `학생 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `학생 로그인 / 이용 내역 확인 </td></tr>
<tr><td colspan="1" valign="top"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자(학생회) </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top"><p>` `학생은 시스템에 로그인 되어 있어야 한다. </p><p>` `학생은 신청하려는 사물함이 현재 사용 중이지 않아야 한다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top"><p>` `학생은 신청한 사물함을 사용할 수 있게 된다. </p><p>` `학생이 신청한 사물함은 사용중인 사물함으로 바뀌어야한다. </p></td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1"><p>1. 학생이 사용하고 싶은 사물함을  선택한다. </p><p>2. 학생은 신청한 사물함을 사용할 수  있다. </p></td><td colspan="1"><p>1.1. 요청한 정보를 시스템이 수신한다. </p><p>1.2. 해당 사물함을 해당 학생에게 </p><p>` `배정한다. </p><p>2\.1. 시스템은 반납과 이용내역 확인을  할 수 있는 화면을 보여준다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top">1\. 학생이 이미 신청된 사물함을 선택한 경우 : 이미 신청된 사물함을 선택할 수  없게 한다. </td></tr>
</table>

Use Case 3 : 사물함 반납 
<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `사물함 반납 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `학생이 사용 중인 사물함을 반납한다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `학생이 사용 중인 사물함을 반납하고자 한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `학생이 반납을 요청하면, 시스템은 사물함에 배정된 학생을 초기화하고, 해당  사물함은 사용 가능한 상태가 된다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `학생 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `학생 로그인 / 이용 내역 확인 </td></tr>
<tr><td colspan="1" valign="top"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자(학생회) </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top"><p>` `학생은 시스템에 로그인 되어 있어야 한다. </p><p>` `반납하려는 사물함이 학생이 신청했던 사물함이어야 한다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `학생이 사용 중이였던 사물함은 사용 가능한 상태가 된다.  시스템은 사물함 상태를 변경한다. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1"><p>1. 학생이 사용하던 사물함을 반납  신청한다. </p><p>2. 학생은 반납 완료 되었다는 것을  확인한다. </p></td><td colspan="1"><p>1.1. 요청한 정보를 시스템이 수신한다. </p><p>1.2. 사물함에 저장되어 있던 학생 </p><p>` `정보를 삭제한다. </p><p>1.3. 사물함 상태를 사용가능하게 </p><p>` `변경한다. </p><p>2\.1. 시스템은 사물함 신청을 할 수 있는  화면을 보여준다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top">1\. 사물함을 신청하지 않은 학생이 반납을 신청할 경우: 사물함을 신청하지 않은  학생은 반납을 할 수 있는 페이지에 접근하지 못하게 한다. </td></tr>
</table>


Use Case 4 : 이용 내역 확인 



<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `이용 내역 확인 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `학생이 자신이 사용한 사물함의 이용 내역을 확인한다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `학생이 자신의 계정으로 로그인 후, 이용 내역 확인을 선택한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `학생이 이용 내역 확인을 선택하면, 현재 사용중인 사물함을 확인할 수 있다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `학생 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `학생 로그인 / 사물함 신청 / 사물함 반납 </td></tr>
<tr><td colspan="1" valign="top"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자(학생회) </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `학생은 시스템에 로그인 되어 있어야 한다.  학생이 사물함을 사용 중이어야 한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `학생은 사용 중인 사물함을 확인할 수 있다. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1" valign="top"><p>1. 학생이 로그인을 한다. </p><p>2. 학생이 이용 내역 확인을 선택한다. </p></td><td colspan="1" valign="top"><p>1\.1. 시스템이 학생 정보를 확인한다. </p><p>2\.1. 시스템이 해당 학생이 사용중인  사물함 정보를 출력한다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top">1\. 사물함을 신청하지 않은 학생이 이용 내역을 확인할 경우: 사물함을 신청하지  않은 학생은 이용 내역 확인을 할 수 있는 페이지에 접근하지 못하게 한다. </td></tr>
</table>

Use Case 5 : 관리자 로그인 



<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `관리자(학생회) 로그인 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `관리자가 학번과 비밀번호를 입력하여 로그인한다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `관리자가 로그인을 시도한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `관리자가 학번과 비밀번호를 입력하여 시스템에 로그인한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `사물함 목록 확인 / 사물함 할당 및 반납 / 학생 목록 확인 </td></tr>
<tr><td colspan="1" valign="top"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `관리자는 학번과 비밀번호가 시스템에 학생과 별도로 등록되어 있어야 한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `관리자는 시스템에 로그인되어 있다. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1"><p>1. 로그인 페이지에 접속한다. </p><p>2. 학번과 비밀번호를 입력한다. </p><p>3. 로그인 버튼을 클릭한다. </p></td><td colspan="1"><p>1\.1. 로그인 페이지를 보여준다. </p><p>2\.1. 입력된 학번과 비밀번호를 </p><p>` `확인한다. </p><p>3\.1. 관리자 계정으로 로그인한다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top"><p>2\.1. 학번이나 비밀번호를 잘못 입력한 경우: 입력한 정보가 시스템에 등록되어 </p><p>` `있는 정보와 일치하지 않으면 로그인이 실패한다. </p><p>2\.1. 시스템에 등록되지 않은 학번인 경우: 입력한 학번이 시스템에 등록되어 </p><p>` `있지 않으면 로그인이 실패한다. </p><p>2\.1. 입력된 학번과 비밀번호가 관리자로 등록된 사람이 아니고 일반 학생일 경우 </p><p>: 학생 로그인으로 넘어간다. </p></td></tr>
</table>

Use Case 6 : 사물함 목록 확인 



<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `사물함 목록 확인 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `관리자에게 현재 사용중인 사물함 목록과 사용 가능한 사물함 목록을 보여준다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `관리자가 자신의 계정으로 로그인한 후, 사물함 목록 확인을 선택한다. </td></tr>
<tr><td colspan="1" valign="top"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2" valign="top">` `관리자가 사물함 목록 확인을 선택하면, 시스템에 등록된 모든 사물함 목록과  어떤 사물함이 사용중이고, 사용 가능한지까지 확인할 수 있다. </td></tr>
<tr><td colspan="1" valign="top"><b>Actors (</b>액터<b>)</b> </td><td colspan="2" valign="top">` `관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `관리자 로그인 / 사물함 할당 및 반납 </td></tr>
<tr><td colspan="1" valign="top"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top"><p>` `관리자는 시스템에 로그인되어 있어야 한다. </p><p>` `시스템은 모든 사물함 목록을 가지고 있어야 한다. </p><p>` `시스템은 모든 사물함의 현재 상태(사용중, 사용 가능)를 알고 있어야 한다. </p></td></tr>
<tr><td colspan="1" valign="top"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2" valign="top">` `관리자는 현재 사용중인 사물함 목록과 사용 가능한 사물함 목록을 확인할 수  있다. </td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1"><p>1. 관리자가 사물함 목록 확인을  선택한다. </p><p>2. 관리자가 사물함 목록을 확인할 수  있다. </p></td><td colspan="1" valign="top">1\.1. 현재 사용중인 사물함 목록과 사용  가능한 사물함 목록을 데이터베이스에서  조회 후 화면에 보여준다. </td></tr>
<tr><td colspan="1" valign="top"><b>Exception conditions (</b>예외</b>  처리<b>)</b> </td><td colspan="2" valign="top">1\.1. 시스템에 문제가 발생하여 사물함 목록을 조회할 수 없는 경우 : 관리자에게  에러 메시지를 표시해준다. </td></tr>
</table>

Use Case 7 : 사물함 할당 및 반납 



<table><tr><th colspan="1" valign="top"><b>Use Case name (</b>유스</b> 케이스</b> 이름<b>)</b> </th><th colspan="2" valign="top">` `사물함 할당 및 반납 </th></tr>
<tr><td colspan="1" valign="top"><b>Scenario (</b>시나리오<b>)</b> </td><td colspan="2" valign="top">` `관리자가 학생에게 사용 가능한 사물함들 중 하나를 할당해주거나, 학생이  사용하고 있는 사물함을 반납시킨다. </td></tr>
<tr><td colspan="1" valign="top"><p><b>Triggering event</b> </p><p><b>(Use Case</b>를</b> </p><p></b> 시작시키는</b> 상황<b>)</b> </p></td><td colspan="2" valign="top">` `관리자가 자신의 계정으로 로그인한 후, 사물함 할당 및 반납을 선택한다. </td></tr>
<tr><td colspan="1"><b>Brief description (</b>간략한</b> 설명<b>)</b> </td><td colspan="2"><p>` `관리자가 사물함 할당 및 반납을 선택하면 원하는 학생에게 사용 가능한 사물함들  중 하나를 정해 할당해주거나, 학생이 사용하고 있는 사물함을 강제로 반납시킬 </p><p>` `수 있다. </p></td></tr>
<tr><td colspan="1"><b>Actors (</b>액터<b>)</b> </td><td colspan="2">` `관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Related use cases (</b>관련된</b>  유스</b> 케이스<b>)</b> </td><td colspan="2" valign="top">` `관리자 로그인 / 학생 목록 확인 </td></tr>
<tr><td colspan="1"><b>Stakeholders (</b>요구사항을</b> 제시한</b>  사람<b>)</b> </td><td colspan="2" valign="top">` `학생, 관리자 </td></tr>
<tr><td colspan="1" valign="top"><b>Preconditions (</b>사전</b> 조건<b>)</b> </td><td colspan="2" valign="top"><p>` `관리자는 시스템에 로그인되어 있어야 한다. </p><p>` `시스템은 모든 사물함 목록을 가지고 있어야 한다. </p><p>` `시스템은 모든 사물함의 현재 상태(사용중, 사용 가능)를 알고 있어야 한다.  시스템은 모든 학생의 목록을 가지고 있어야 한다. </p></td></tr>
<tr><td colspan="1"><b>Postconditions (</b>사후</b> 조건<b>)</b> </td><td colspan="2"><p>` `관리자가 할당해준 학생에게 선택된 사물함이 할당된다. </p><p>` `관리자가 강제로 반납시킨 사물함이 다시 사용 가능한 상태가 된다. </p></td></tr>
<tr><td colspan="1" rowspan="2" valign="top"><b>Flow of activities (</b>주</b> 사건</b> 흐름<b>)</b> </td><td colspan="1">Actor </td><td colspan="1">System </td></tr>
<tr><td colspan="1" valign="top"><p>1. 관리자가 사물함 할당 및 반납을  선택한다. </p><p>2. 관리자가 사물함을 선택한다. </p><p>3. 관리자가 사물함 반납을 선택한다. </p><p>4. 관리자가 사물함을 선택한다. </p><p>5. 관리자가 사물함을 할당해줄  학생을 선택한다. </p></td><td colspan="1" valign="top"><p>1\.1. 현재 사용중인 사물함 목록과 사용 </p><p>` `가능한 사물함 목록을 데이터베이스에서  조회 후 화면에 보여준다. </p><p>2\.1. 사용중인 사물함이라면 강제 </p><p>` `반납시킬 것인지 여부를 확인한다. </p><p>3\.1 사물함이 강제로 반납되고, 사물함이  사용 가능한 상태로 변경된다. </p><p>4\.1 사용 가능한 사물함이라면 어떤 </p><p>` `학생에게 할당할 것인지 학생 리스트를 </p><p>` `보여준다. </p><p>5\.1 사물함이 선택한 학생에게 할당되고,  사물함이 사용중인 상태로 변경된다. </p></td></tr>
</table>



|**Exception conditions (**예외**  처리**)** |<p>1\.1. 시스템에 문제가 발생하여 사물함 목록을 조회할 수 없는 경우 : 관리자에게  에러 메시지를 표시해준다. </p><p>4\.1. 시스템에 문제가 발생하여 학생 목록을 조회할 수 없는 경우 : 관리자에게 </p><p>` `에러 메시지를 표시해준다. </p><p>5\.1. 선택한 학생이 이미 다른 사물함을 사용중일 경우 : 관리자에게 선택한 </p><p>` `학생이 이미 사물함을 사용중이라는 에러 메시지를 표시해준다. </p>|
| :- | :- |

Use Case 8 : 학생 목록 확인 



|**Use Case name (**유스** 케이스** 이름**)** |` `학생 목록 확인 ||
| - | - | :- |
|**Scenario (**시나리오**)** |` `관리자에게 등록된 학생 목록을 보여준다. ||
|<p>**Triggering event** </p><p>**(Use Case**를** </p><p>** 시작시키는** 상황**)** </p>|` `관리자가 자신의 계정으로 로그인한 후, 학생 목록 확인을 선택한다. ||
|**Brief description (**간략한** 설명**)** |` `관리자가 학생 목록 확인을 선택하면, 시스템에 등록된 모든 학생의 목록과 그  학생이 사물함을 사용중인지의 여부를 확인할 수 있다. ||
|**Actors (**액터**)** |` `관리자 ||
|**Related use cases (**관련된**  유스** 케이스**)** |` `관리자 로그인 / 사물함 목록 확인 ||
|**Stakeholders (**요구사항을** 제시한**  사람**)** |` `학생, 관리자 ||
|**Preconditions (**사전** 조건**)** |<p>` `관리자는 시스템에 로그인되어 있어야 한다. </p><p>` `시스템은 모든 사물함 목록을 가지고 있어야 한다. </p><p>` `시스템은 모든 사물함의 현재 상태(사용중, 사용 가능)를 알고 있어야 한다.  시스템은 모든 학생의 목록을 가지고 있어야 한다. </p>||
|**Postconditions (**사후** 조건**)** |` `관리자는 데이터베이스에 등록된 모든 학생 목록을 확인할 수 있고, 모든  학생들이 현재 사물함 사용중인지의 여부를 확인할 수 있다. ||
|**Flow of activities (**주** 사건** 흐름**)** |Actor |System |



||<p>1. 관리자가 학생 목록 확인을  선택한다. </p><p>2. 관리자가 학생 목록과 사물함  사용중 여부를 확인할 수 있다. </p>|<p>1\.1. 등록된 모든 학생의 목록과  학생들의 사물함 사용중 여부를 </p><p>` `데이터베이스에서 조회 후 화면에  보여준다. </p>|
| :- | :- | - |
|**Exception conditions (**예외**  처리**)** |<p>1\.1. 시스템에 문제가 발생하여 학생 목록을 조회할 수 없는 경우 : 관리자에게  에러 메시지를 표시해준다. </p><p>1\.1. 시스템에 문제가 발생하여 학생의 사물함 사용중 여부를 조회할 수 없는  경우 : 관리자에게 에러 메시지를 표시해준다. </p>||

3. Use Case Diagram 그리기 ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.004.png)

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.005.jpeg)

4. 비기능적 요구사항 도출 



|**NFR** 내용** |** 고려하는 **Quality (**혹은 **quality**의 **sub-characteristic)** |**Quality Attributes** |
| - | :- | - |
|` `로그인 시스템  안정성 유지 |Reliability - Fault Tolerance |` `로그인 시스템 장애가 발생할 경우, 에러  메시지를 출력하도록 함. |
|` `사물함 신청 및  반납 처리 시간  단축 |Efficiency - Time Behavior |` `사물함 신청 및 반납 요청에 대한 응답 시간이  평균 3초 이내로 유지되도록 함. |
|<p>` `학생 및 관리자 </p><p>` `인터페이스 직관성  제공 </p>|Usability - Understandability |` `학생 및 관리자 인터페이스가 직관적이고  이해하기 쉽도록 함. |
|` `시스템 보안 강화 |Functionality - Security |<p>` `개인정보(학번, 비밀번호) 및 시스템 데이터에  대한 접근 및 노출 방지를 위해 적절한 보안 </p><p>` `조치를 적용함. </p>|
|<p>` `학생 및 관리자 </p><p>` `로그인 처리 시간  최소화 </p>|Efficiency - Time Behavior |` `로그인 요청에 대한 응답 시간이 평균 3초  이내로 유지되도록 함. |
|` `서버 용량 및 성능  유지 |Maintainability - Changeability |<p>` `서버가 최소 100명의 동시 접속 요청에 대해 </p><p>` `안정적으로 처리할 수 있도록 하며, 서비스 확장  시 서버의 성능을 유지할 수 있도록 함. </p>|
|<p>` `학생 및 관리자가  이용 내역을 </p><p>` `신뢰할 수 있도록  함 </p>|Functionality - Accurateness |<p>` `이용 내역이 정확하게 기록되어 있으며, </p><p>` `시스템에서 제공되는 이용 내역은 학생 및  관리자가 신뢰할 수 있도록 함. </p>|

3. **Domain Model** 설계하기 **![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.006.png)**



|**Class** 명** |**Concept** 설명** |** 주요 **Attributes** |
| - | - | - |
|Student |` `학생을 나타내는 Class로,  학생이 로그인하고 사물함을  신청하거나 반납할 수 있다. |ID, Password, 학번, 학생이 현재 사용중인  사물함 번호 정보 |
|Admin |` `관리자를 나타내는 클래스로,  관리자가 로그인하고 사물함을  할당하거나 반납받을 수 있다. |ID, Password, 학번 |
|Locker |<p>` `사물함을 나타내는 클래스로,  사용 가능한 사물함과 사용 </p><p>` `중인 사물함을 구분한다. </p>|` `사물함의 번호 정보, 해당 사물함의 사용 가능  여부 정보 |
|DB Manager |` `데이터베이스를 관리하는  클래스로, 학생과 사물함  정보를 관리한다. |` `학생 정보를 저장하는 DB 정보, 사물함 정보를  저장하는 DB 정보 |
|Program UI |<p>` `프로그램의 사용자 </p><p>` `인터페이스를 나타내는 </p><p>` `클래스로, 사용자가 프로그램을  조작할 수 있다. </p>|` `학생 및 관리자 로그인 화면 UI, 사물함 신청 및  반납 화면 UI, 관리자 메뉴 화면 UI |

4. **Design Model** 설계하기** 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.007.jpeg)

Operation Contract 

System operation: Locker Submit() 

Responsibility : 학생이 사용할 수 있는 사물함을 확인하고 사물함 신청을 위해 시스템에 요청하고, 해당  사물함을 사용할 수 있게 된다. 

Pre-conditions : 

- 학생은 시스템에 로그인 되어 있어야 한다. 
- 학생은 신청하려는 사물함이 현재 사용 중이지 않아야 한다. 

Post-conditions : 

- 학생은 신청한 사물함을 사용할 수 있게 된다. 
- 학생이 신청한 사물함은 사용중인 사물함으로 바뀌어야한다. 

System : 

- +applyBtn(studentDB : StudentDB) 
- +insertLockerNum(name : str, locker\_num : Locker) 
- +insertStudent(name : str, locker\_num : Locker) 
- +getLockerNum() : str 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.008.jpeg)

![ref1]

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.010.jpeg)

Operation Contract 

System operation : Locker Return() 

Responsibility :  학생이 반납을 요청하면, 시스템은 사물함에 배정된 학생을 초기화하고, 해당 사물함은  사용 가능한 상태가 된다. 

Pre-conditions : 

- 학생은 시스템에 로그인 되어 있어야 한다. 
- 반납하려는 사물함이 학생이 신청했던 사물함이어야 한다. 

Post-conditions : 

- 학생이 사용 중이였던 사물함은 사용 가능한 상태가 된다. 
- 시스템은 사물함 상태를 변경한다. 

System : 

- +returnBtn(studentDB : StudentDB) 
- +deleteLockerNum(name : str, locker\_num : Locker) 
- +deleteStudent(name : str, locker\_num : Locker) 
- +getLockerNum() : str 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.011.jpeg)

![ref2]

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.013.jpeg)

Operation Contract 

System operation : Locker Checking() 

Responsibility :  관리자가 사물함 목록 확인을 선택하면, 시스템에 등록된 모든 사물함 목록과 어떤  사물함이 사용중이고, 사용 가능한지까지 확인할 수 있다. 

Pre-conditions : 

- 관리자는 시스템에 로그인되어 있어야 한다. 
- 시스템은 모든 사물함 목록을 가지고 있어야 한다. 
- 시스템은 모든 사물함의 현재 상태(사용중, 사용 가능)를 알고 있어야 한다. 

Post-conditions : 

- 관리자는 현재 사용중인 사물함 목록과 사용 가능한 사물함 목록을 확인할 수 있다. 

System : 

- getLockerDBBtn(lockerDB) 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.014.jpeg)

![ref1]

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.015.jpeg)

Operation Contract 

System operation : Student Checking() 

Responsibility :  관리자가 학생 목록 확인을 선택하면, 시스템에 등록된 모든 학생의 목록과 그 학생이  사물함을 사용중인지의 여부를 확인할 수 있다. 

Pre-conditions : 

- 관리자는 시스템에 로그인되어 있어야 한다. 
- 시스템은 모든 사물함 목록을 가지고 있어야 한다. 
- 시스템은 모든 사물함의 현재 상태(사용중, 사용 가능)를 알고 있어야 한다. 
- 시스템은 모든 학생의 목록을 가지고 있어야 한다. 

Post-conditions : 

- 관리자는 데이터베이스에 등록된 모든 학생 목록을 확인할 수 있고, 모든 학생들이 현재 사물함  사용중인지의 여부를 확인할 수 있다. 

System : 

- getStudentDBBtn(studentDB) 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.016.jpeg)

![ref2]

5. **Design Model** 설계하기 **(Class Diagram) ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.017.png)**

**5.1 Class Diagram GRASP** 적용 **![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.018.png)**

6. **SW Design Pattern**을** 적용한 **Class Diagram ![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.019.png)**
7. **Design Refinement** 표** 



|<p>Before </p><p>` `단계의 Class 등  설계 classifier </p>|After 단계의 Class 등 설계 classifier(s) |` `적용한 설계 개념 (GRASP, Design Pattern  적용) |Architecture Design Rationale (본인이 생각하는  합리성) |NFR 와 QA 에  대한 영향 분석 |
| - | :- | :- | :- | :- |
|LockerDB, StudentDB, |LockerDBController, AdminDBController, StudentDBController |<p>GRASP </p><p>` `원리에서 Controller, Information Expert 개념 적용 </p>|<p>DB에 인스턴스를  저장하는 클래스로  다른 컴포넌트의 </p><p>` `변경에 영향을 </p><p>` `받지 않고 </p><p>` `재사용이 가능합니  다. </p>|<p>` `사용자 입력을 </p><p>` `처리하고 시스템 </p><p>` `동작을 처리하는 Controller와 특정  정보를 가지고 </p><p>` `있는 클래스에 </p><p>` `책임을 부여하는 Information Expert는 </p><p>` `시스템의 Performance와 Security, Maintainability의  성능을 </p><p>` `향상시키는데 </p><p>` `기여합니다. </p>|
|Locker, Admin, Student |Locker, Admin, Student |<p>GRASP </p><p>` `원리에서 Creator, Pure Fabrication 개념  적용 </p>|<p>` `객체 생성을 </p><p>` `담당하는 클래스로 Controller 클래 </p><p>` `스의 대한 기본 </p><p>` `속성입니다. </p>|<p>` `객체 생성에 대한  책임을 관리하는 Creator와 도메인 </p><p>` `개념이나 역할을  가지지 않는 </p><p>` `객체에 책임을 </p><p>` `할당하는 Pure Fabrication은 </p><p>` `객체 생성을 </p><p>` `최적화하고 </p><p>` `의존성을 줄여 Performance와 Reusability의 </p><p>` `성능을 </p><p>` `향상시키는데 </p><p>` `기여합니다. </p>|



|LoginWind ow, ApplyWind ow, AdminWind ow, ReturnWin dow |LoginWindow, ApplyWindow, AdminWindow, ReturnWindow |<p>GRASP </p><p>` `원리에서 Information Expert 적용, GoF Design Pattern에서 Facade Pattern  적용 </p>|<p>` `사용자에게 </p><p>` `보여지는 User Interface로 </p><p>UI 계층에서 </p><p>` `사용자의 입력을 </p><p>` `받아 Controller에  게 로직을 </p><p>` `분기해서 </p><p>` `처리합니다. </p><p>` `책임을 수행할 수  있는 데이터를 </p><p>` `가지고 있는 </p><p>` `객체에게 책임을 </p><p>` `부여합니다. </p>|<p>` `특정 정보를 </p><p>` `가지고 있는 </p><p>` `클래스에 책임을 </p><p>` `부여하는 Information Expert와 복잡한  시스템 또는 </p><p>` `서브시스템을 </p><p>` `단순화하여 외부에  통합된 단일 </p><p>` `인터페이스를 </p><p>` `제공하는 Facade Pattern은 </p><p>` `인터페이스가 </p><p>` `직관적이고 </p><p>` `이해하기 쉽도록 </p><p>` `하고 Performance와 Maintainability의  성능 향상에 </p><p>` `기여합니다. 성능,  유지보수성, </p><p>` `코드의 가독성과 </p><p>` `유연성 등의 </p><p>` `측면에서 Information Expert와 Facade Pattern의 적절한  적용은 소프트웨어  시스템의 품질을 </p><p>` `향상시키는데 </p><p>` `기여할 수 </p><p>` `있습니다. </p>|
| :- | :- | - | - | - |

8. 결과 **Snapshot** 

` `프로그램을 실행하면 로그인 화면이 보여집니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.020.jpeg)

` `로그인을 하게 되면 사물함 신청 페이지가 뜨게 됩니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.021.jpeg) 신청 가능한 사물함을 확인한 후 선택하고 신청하기 버튼을 누르면 사물함 신청이  완료됩니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.022.jpeg)

` `사물함 신청을 하게 되면 사물함 반납과 이용 내역을 확인할 수 있는 페이지 로  넘어가게 됩니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.023.jpeg)

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.024.jpeg)

` `사물함 반납하기를 완료하면 다시 사물함 신청 화면으로 돌아오게 되고, 사용중이던 A-1 사물함은 다시 사용 가능으로 바뀌게 된 것을 볼 수 있습니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.025.jpeg)

AdminDB에 등록되어 있는 계정일 경우, 관리자 로그인을 할 수 있습니 다. 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.026.jpeg)

` `관리자는 사용중인 사물함을 반납시 키거나 , 사용중이지 않은 사물함에 학생을  할당할 수 있고, 학생 목록을 확인할 수 있습니다 . 

![](Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.027.jpeg)

[ref1]: Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.009.png
[ref2]: Aspose.Words.a6a4de41-fe18-4057-b32e-df1ddd50b598.012.png

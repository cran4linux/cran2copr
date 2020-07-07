%global packname  studentlife
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Tidy Handling and Navigation of the Student-Life Dataset

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-R.utils >= 2.8.0
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-skimr >= 1.0.5
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-visdat >= 0.5.3
BuildRequires:    R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-R.utils >= 2.8.0
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-skimr >= 1.0.5
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-visdat >= 0.5.3
Requires:         R-CRAN-purrr >= 0.3.2

%description
Download, navigate and analyse the Student-Life dataset. The Student-Life
dataset contains passive and automatic sensing data from the phones of a
class of 48 Dartmouth college students. It was collected over a 10 week
term. Additionally, the dataset contains ecological momentary assessment
results along with pre-study and post-study mental health surveys. The
intended use is to assess mental health, academic performance and
behavioral trends. The raw dataset and additional information is available
at <https://studentlife.cs.dartmouth.edu/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

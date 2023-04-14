%global __brp_check_rpaths %{nil}
%global packname  odk
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Convert 'ODK' or 'XLSForm' to 'SPSS' Data Frame

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gsheet 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-utils 
Requires:         R-CRAN-gsheet 
Requires:         R-CRAN-openxlsx 
Requires:         R-utils 

%description
After develop a 'ODK' <https://opendatakit.org/> frame, we can link the
frame to 'Google Sheets' <https://www.google.com/sheets/about/> and
collect data through 'Android' <https://www.android.com/>. This data
uploaded to a 'Google sheets'. odk2spss() function help to convert the
'odk' frame into 'SPSS'
<https://www.ibm.com/analytics/us/en/technology/spss/> frame. Also able to
add downloaded 'Google sheets' data or read data from 'Google sheets' by
using 'ODK' frame 'submission_url'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

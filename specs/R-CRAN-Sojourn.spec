%global packname  Sojourn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Apply Sojourn Methods for Processing ActiGraph AccelerometerData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-svDialogs >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.2
BuildRequires:    R-CRAN-AGread 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-nnet >= 7.3
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-svDialogs >= 1.0
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-rlang >= 0.2
Requires:         R-CRAN-AGread 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a simple way for utilizing Sojourn methods for accelerometer
processing, as detailed in Lyden K, Keadle S, Staudenmayer J, & Freedson P
(2014) <doi:10.1249/MSS.0b013e3182a42a2d>, Ellingson LD, Schwabacher IJ,
Kim Y, Welk GJ, & Cook DB (2016) <doi:10.1249/MSS.0000000000000915>, and
Hibbing PR, Ellingson LD, Dixon PM, & Welk GJ (2018)
<doi:10.1249/MSS.0000000000001486>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

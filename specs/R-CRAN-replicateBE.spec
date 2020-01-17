%global packname  replicateBE
%global packver   1.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}
Summary:          Average Bioequivalence with Expanding Limits (ABEL)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PowerTOST >= 1.3.3
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-PowerTOST >= 1.3.3
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-lmerTest 
Requires:         R-nlme 
Requires:         R-CRAN-pbkrtest 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Performs comparative bioavailability calculations for Average
Bioequivalence with Expanding Limits (ABEL). Implemented are 'Method A'
and 'Method B' and the detection of outliers. If the design allows,
assessment of the empiric Type I Error and iteratively adjusting alpha to
control the consumer risk. Average Bioequivalence - optionally with a
tighter (narrow therapeutic index drugs) or wider acceptance range (Gulf
Cooperation Council, South Africa: Cmax) - is implemented as well.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

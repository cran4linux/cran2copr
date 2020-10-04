%global packname  mlt
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Most Likely Transformations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-basefun >= 1.0.5
BuildRequires:    R-CRAN-variables >= 1.0.2
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-basefun >= 1.0.5
Requires:         R-CRAN-variables >= 1.0.2
Requires:         R-CRAN-BB 
Requires:         R-CRAN-alabama 
Requires:         R-stats 
Requires:         R-CRAN-coneproj 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-numDeriv 
Requires:         R-survival 
Requires:         R-CRAN-nloptr 

%description
Likelihood-based estimation of conditional transformation models via the
most likely transformation approach described in Hothorn et al. (2018)
<DOI:10.1111/sjos.12291>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX

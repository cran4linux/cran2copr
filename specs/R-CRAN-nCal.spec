%global packname  nCal
%global packver   2020.5-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.5.21
Release:          3%{?dist}
Summary:          Nonlinear Calibration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-kyotil 
BuildRequires:    R-CRAN-gWidgets2 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-kyotil 
Requires:         R-CRAN-gWidgets2 

%description
Performs nonlinear calibration and curve fitting for data from Luminex,
RT-PCR, ELISA, RPPA etc. Its precursor is Ruminex. This package is
described in Fong et al. (2013) <DOI:10.1093/bioinformatics/btt456>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/jags_script
%doc %{rlibdir}/%{packname}/misc
%doc %{rlibdir}/%{packname}/otherTests
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX

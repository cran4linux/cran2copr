%global __brp_check_rpaths %{nil}
%global packname  weightedScores
%global packver   0.9.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted Scores Method for Regression Models with Dependent Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rootSolve 

%description
The weighted scores method and composite likelihood information criteria
as an intermediate step for variable/correlation selection for
longitudinal ordinal and count data in Nikoloulopoulos, Joe and Chaganty
(2011) <doi:10.1093/biostatistics/kxr005>, Nikoloulopoulos (2016)
<doi:10.1002/sim.6871> and Nikoloulopoulos (2017) <arXiv:1510.07376>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

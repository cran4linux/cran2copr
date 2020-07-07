%global packname  DiPs
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}
Summary:          Directional Penalties for Optimal Matching in ObservationalStudies

License:          MIT+file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-liqueueR 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-liqueueR 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-methods 

%description
Improves the balance of optimal matching with near-fine balance by giving
penalties on the unbalanced covariates with the unbalanced directions.
Many directional penalties can also be viewed as Lagrange multipliers,
pushing a matched sample in the direction of satisfying a linear
constraint that would not be satisfied without penalization. Yu, R., and
Rosenbaum, P. R. (2019). <doi:10.1111/biom.13098>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

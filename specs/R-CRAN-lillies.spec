%global packname  lillies
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          3%{?dist}
Summary:          Estimation of Life Years Lost

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ddpcr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ddpcr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Estimation of life expectancy and Life Years Lost (LYL, or lillies for
short) for a given population, for example those with a given disease or
condition. In addition, the package can be used to compare estimates from
different populations, or to estimate confidence intervals. Technical
details of the method are available in Plana-Ripoll et al. (2020)
<doi:10.1371/journal.pone.0228073> and Andersen (2017)
<doi:10.1002/sim.7357>.

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

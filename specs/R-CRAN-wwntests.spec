%global __brp_check_rpaths %{nil}
%global packname  wwntests
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Hypothesis Tests for Functional Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ftsa 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
Requires:         R-CRAN-sde 
Requires:         R-stats 
Requires:         R-CRAN-ftsa 
Requires:         R-CRAN-rainbow 
Requires:         R-MASS 
Requires:         R-graphics 

%description
Provides an array of white noise hypothesis tests for functional data and
related visualizations. These include tests based on the norms of
autocovariance operators that are built under both strong and weak white
noise assumptions. Additionally, tests based on the spectral density
operator and on principal component dimensional reduction are included,
which are built under strong white noise assumptions. These methods are
described in Kokoszka et al. (2017) <doi:10.1016/j.jmva.2017.08.004>,
Characiejus and Rice (2019) <doi:10.1016/j.ecosta.2019.01.003>, and Gabrys
and Kokoszka (2007) <doi:10.1198/016214507000001111>, respectively.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

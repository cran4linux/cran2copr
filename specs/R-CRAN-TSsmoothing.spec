%global packname  TSsmoothing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Trend Estimation of Univariate and Bivariate Time Series withControlled Smoothness

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-Matrix >= 1.2.0
Requires:         R-MASS >= 7.3.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-Matrix >= 1.2.0

%description
It performs the smoothing approach provided by penalized least squares for
univariate and bivariate time series, as proposed by Guerrero (2007) and
Gerrero et al. (2017). This allows to estimate the time series trend by
controlling the amount of resulting (joint) smoothness. --- Guerrero, V.M
(2007) <DOI:10.1016/j.spl.2007.03.006>. Guerrero, V.M; Islas-Camargo, A.
and Ramirez-Ramirez, L.L. (2017) <DOI:10.1080/03610926.2015.1133826>.

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

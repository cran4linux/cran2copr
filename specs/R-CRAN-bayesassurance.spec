%global __brp_check_rpaths %{nil}
%global packname  bayesassurance
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Assurance Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.55
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-stats >= 4.0.5
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-mathjaxr >= 1.5.2
BuildRequires:    R-CRAN-pbapply >= 1.5.0
BuildRequires:    R-CRAN-plot3D >= 1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-MASS >= 7.3.55
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-stats >= 4.0.5
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-mathjaxr >= 1.5.2
Requires:         R-CRAN-pbapply >= 1.5.0
Requires:         R-CRAN-plot3D >= 1.4
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-rlang >= 1.0.2

%description
Computes Bayesian assurance under various settings characterized by
different assumptions and objectives, including precision-based
conditions, credible intervals, and goal functions. All simulation-based
functions included in this package rely on a two-stage Bayesian method
that assigns two distinct priors to evaluate the probability of observing
a positive outcome, which addresses subtle limitations that take place
when using the standard single-prior approach. For more information,
please refer to Pan and Banerjee (2021) <arXiv:2112.03509>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

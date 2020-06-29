%global packname  rewie
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Data Preparation and Diagnostics for Random Effects WithinEstimator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rockchalk 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-stats 
Requires:         R-CRAN-rockchalk 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-CRAN-plm 
Requires:         R-stats 

%description
Diagnostics and data preparation for random effects within estimator,
random effects within-idiosyncratic estimator,
between-within-idiosyncratic model, and cross-classified between model.
Mundlak, Yair (1978) <doi:10.2307/1913646>. Hausman, Jeffrey (1978)
<doi:10.2307/1913827>. Allison, Paul (2009) <doi:10.4135/9781412993869>.
Neuhaus, J.M., and J. D. Kalbfleisch (1998) <doi:10.2307/3109770>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

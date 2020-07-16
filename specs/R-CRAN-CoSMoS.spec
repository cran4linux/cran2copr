%global packname  CoSMoS
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Complete Stochastic Modelling Solution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mAr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-MBA 
Requires:         R-Matrix 
Requires:         R-CRAN-mAr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-pracma 

%description
A single framework, unifying, extending, and improving a general-purpose
modelling strategy, based on the assumption that any process can emerge by
transforming a specific 'parent' Gaussian process Papalexiou (2018)
<doi:10.1016/j.advwatres.2018.02.013>.

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

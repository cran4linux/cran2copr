%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inphr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Persistence Homology Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fdatest 
BuildRequires:    R-CRAN-flipr 
BuildRequires:    R-CRAN-phutil 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-TDAvec 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fdatest 
Requires:         R-CRAN-flipr 
Requires:         R-CRAN-phutil 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-TDAvec 

%description
A set of functions for performing null hypothesis testing on samples of
persistence diagrams using the theory of permutations. Currently, only
two-sample testing is implemented. Inputs can be either samples of
persistence diagrams themselves or vectorizations. In the former case,
they are embedded in a metric space using either the Bottleneck or
Wasserstein distance. In the former case, persistence data becomes
functional data and inference is performed using tools available in the
'fdatest' package. Main reference for the interval-wise testing method:
Pini A., Vantini S. (2017) "Interval-wise testing for functional data"
<doi:10.1080/10485252.2017.1306627>. Main reference for inference on
populations of networks: Lovato, I., Pini, A., Stamm, A., & Vantini, S.
(2020) "Model-free two-sample test for network-valued data"
<doi:10.1016/j.csda.2019.106896>.

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

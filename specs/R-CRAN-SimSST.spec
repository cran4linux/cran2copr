%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimSST
%global packver   0.0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Simulated Stop Signal Task Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gamlss.dist 

%description
Stop signal task data of go and stop trials is generated per participant.
The simulation process is based on the independent horse race model and
fixed stop signal delay or tracking method. Each of go and stop process is
assumed having exponentially modified Gaussian(ExG) or Shifted Wald (SW)
distributions. The output data can be converted to 'BEESTS' software input
data enabling researchers to test and evaluate various brain stopping
processes manifested by ExG or SW distributional parameters of interest.
Methods are described in: Soltanifar M (2020)
<https://hdl.handle.net/1807/101208>, Matzke D, Love J, Wiecki TV, Brown
SD, Logan GD and Wagenmakers E-J (2013) <doi:10.3389/fpsyg.2013.00918>,
Logan GD, Van Zandt T, Verbruggen F, Wagenmakers EJ. (2014)
<doi:10.1037/a0035230>.

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

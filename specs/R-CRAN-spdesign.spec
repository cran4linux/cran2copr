%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spdesign
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Designing Stated Preference Experiments

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-future 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
Contemporary software commonly used to design stated preference
experiments are expensive and the code is closed source. This is a free
software package with an easy to use interface to make flexible stated
preference experimental designs using state-of-the-art methods. For an
overview of stated choice experimental design theory, see e.g., Rose, J.
M. & Bliemer, M. C. J. (2014) in Hess S. & Daly. A.
<doi:10.4337/9781781003152>. The package website can be accessed at
<https://spdesign.edsandorf.me>. We acknowledge funding from the European
Union’s Horizon 2020 research and innovation program under the Marie
Sklodowska-Curie grant INSPiRE (Grant agreement ID: 793163).

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

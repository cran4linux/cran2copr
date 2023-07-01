%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cbcTools
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Simulation-Based Workflow to Design and Evaluate Choice-Based Conjoint Survey Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-logitr >= 1.0.1
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-idefix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-logitr >= 1.0.1
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-idefix 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
A simulation-based workflow to design and evaluate choice-based conjoint
survey experiments. Generate a variety of survey designs, including full
factorial designs, orthogonal designs, and Bayesian D-efficient designs as
well as designs with "no choice" options and "labeled" (also known as
"alternative specific") designs. Full factorial and orthogonal designs are
obtained using the 'DoE.base' package (Grömping, 2018)
<doi:10.18637/jss.v085.i05>. Bayesian D-efficient designs are obtained
using the 'idefix' package (Traets et al, 2020)
<doi:10.18637/jss.v096.i03>. Conveniently inspect the design balance and
overlap, and simulate choice data for a survey design either randomly or
according to a multinomial or mixed logit utility model defined by
user-provided prior parameters. Conduct a power analysis for a given
survey design by estimating the same model on different subsets of the
data to simulate different sample sizes. Choice simulation and model
estimation in power analyses are handled using the 'logitr' package
(Helveston, 2023) <doi:10.18637/jss.v105.i10>.

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

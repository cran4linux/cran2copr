%global __brp_check_rpaths %{nil}
%global packname  R2BEAT
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multistage Sampling Allocation and Sample Selection

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-glue 

%description
Multivariate optimal allocation for different domains in one and two
stages stratified sample design. R2BEAT extends the Neyman (1934) –
Tschuprow (1923) allocation method to the case of several variables,
adopting a generalization of the Bethel’s proposal (1989).R2BEAT develops
this methodology but, moreover, it allows to determine the sample
allocation in the multivariate and multi-domains case of estimates for
two-stage stratified samples. It also allows to perform both Primary Stage
Units and Secondary Stage Units selection. This package requires the
availability of ReGenesees, that can be installed from
<https://github.com/DiegoZardetto/ReGenesees>.

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

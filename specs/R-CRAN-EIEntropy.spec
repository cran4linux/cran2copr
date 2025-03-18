%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EIEntropy
%global packver   0.0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference Applying Entropy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Implements two estimations related to the foundations of info metrics
applied to ecological inference. These methodologies assess the lack of
disaggregated data and provide an approach to obtaining disaggregated
territorial-level data. For more details, see the following references:
Fernández-Vázquez, E., Díaz-Dapena, A., Rubiera-Morollón, F. et al. (2020)
"Spatial Disaggregation of Social Indicators: An Info-Metrics Approach."
<doi:10.1007/s11205-020-02455-z>. Díaz-Dapena, A., Fernández-Vázquez, E.,
Rubiera-Morollón, F., & Vinuela, A. (2021) "Mapping poverty at the local
level in Europe: A consistent spatial disaggregation of the AROPE
indicator for France, Spain, Portugal and the United Kingdom."
<doi:10.1111/rsp3.12379>.

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

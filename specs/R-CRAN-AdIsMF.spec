%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AdIsMF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adsorption Isotherm Model Fitting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-stats 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nls2 
Requires:         R-stats 

%description
The Langmuir and Freundlich adsorption isotherms are pivotal in
characterizing adsorption processes, essential across various scientific
disciplines. Proper interpretation of adsorption isotherms involves robust
fitting of data to the models, accurate estimation of parameters, and
efficiency evaluation of the models, both in linear and non-linear forms.
For researchers and practitioners in the fields of chemistry,
environmental science, soil science, and engineering, a comprehensive
package that satisfies all these requirements would be ideal for accurate
and efficient analysis of adsorption data, precise model selection and
validation for rigorous scientific inquiry and real-world applications.
Details can be found in Langmuir (1918) <doi:10.1021/ja02242a004> and
Giles (1973) <doi:10.1111/j.1478-4408.1973.tb03158.x>.

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

%global __brp_check_rpaths %{nil}
%global packname  TSS.RESTREND
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Segmentation of Residual Trends

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bfast >= 1.5.7
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-mblm 
Requires:         R-CRAN-bfast >= 1.5.7
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-mblm 

%description
Time Series Segmented Residual Trends is a method for the automated
detection of land degradation from remotely sensed vegetation and climate
datasets. TSS-RESTREND incorporates aspects of two existing degradation
detection methods: RESTREND which is used to control for climate
variability, and BFAST which is used to look for structural changes in the
ecosystem. The full details of the testing and justification of the
TSS-RESTREND method (version 0.1.02) are published in Burrell et al.,
(2017). <doi:10.1016/j.rse.2017.05.018>. The changes to the method
introduced in version 0.2.03 focus on the inclusion of temperature as an
additional climate variable. This allows for land degradation assessment
in temperature limited drylands. A paper that details this work is
currently under review. There are also a number of bug fixes and speed
improvements. Version 0.3.0 introduces additional attribution for eCO2,
climate change and climate variability the details of which are in press
in Burrell et al., (2020).  The version under active development and
additional example scripts showing how the package can be applied can be
found at <https://github.com/ArdenB/TSSRESTREND>.

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

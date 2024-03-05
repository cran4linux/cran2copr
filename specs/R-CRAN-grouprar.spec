%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grouprar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Response Adaptive Randomization for Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-methods 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 

%description
Implement group response-adaptive randomization procedures, which also
integrates standard non-group response-adaptive randomization methods as
specialized instances. It is also uniquely capable of managing complex
scenarios, including those with delayed and missing responses, thereby
expanding its utility in real-world applications. This package offers 16
functions for simulating a variety of response adaptive randomization
procedures. These functions are essential for guiding the selection of
statistical methods in clinical trials, providing a flexible and effective
approach to trial design. Some of the detailed methodologies and
algorithms used in this package, please refer to the following references:
LJ Wei (1979) <doi:10.1214/aos/1176344614> L. J. WEI and S. DURHAM (1978)
<doi:10.1080/01621459.1978.10480109> Durham, S. D., FlournoY, N. AND LI,
W. (1998) <doi:10.2307/3315771> Ivanova, A., Rosenberger, W. F., Durham,
S. D. and Flournoy, N. (2000) <https://www.jstor.org/stable/25053121> Bai
Z D, Hu F, Shen L. (2002) <doi:10.1006/jmva.2001.1987> Ivanova, A. (2003)
<doi:10.1007/s001840200220> Hu, F., & Zhang, L. X. (2004)
<doi:10.1214/aos/1079120137> Hu, F., & Rosenberger, W. F. (2006,
ISBN:978-0-471-65396-7). Zhang, L. X., Chan, W. S., Cheung, S. H., & Hu,
F. (2007) <https://www.jstor.org/stable/26432528> Zhang, L., &
Rosenberger, W. F. (2006) <doi:10.1111/j.1541-0420.2005.00496.x> Hu, F.,
Zhang, L. X., Cheung, S. H., & Chan, W. S. (2008)
<doi:10.1002/cjs.5550360404>.

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

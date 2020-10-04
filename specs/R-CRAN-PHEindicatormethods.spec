%global packname  PHEindicatormethods
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          2%{?dist}%{?buildtag}
Summary:          Common Public Health Statistics and their Confidence Intervals

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Functions to calculate commonly used public health statistics and their
confidence intervals using methods approved for use in the production of
Public Health England indicators such as those presented via Fingertips
(<http://fingertips.phe.org.uk/>). It provides functions for the
generation of proportions, crude rates, means, directly standardised
rates, indirectly standardised rates, standardised mortality ratios, slope
and relative index of inequality and life expectancy. Statistical methods
are referenced in the following publications. Breslow NE, Day NE (1987)
<doi:10.1002/sim.4780080614>. Dobson et al (1991)
<doi:10.1002/sim.4780100317>. Armitage P, Berry G (2002)
<doi:10.1002/9780470773666>. Wilson EB. (1927)
<doi:10.1080/01621459.1927.10502953>. Altman DG et al (2000, ISBN:
978-0-727-91375-3). Chiang CL. (1968, ISBN: 978-0-882-75200-6). Newell C.
(1994, ISBN: 978-0-898-62451-9). Eayres DP, Williams ES (2004)
<doi:10.1136/jech.2003.009654>. Silcocks PBS et al (2001)
<doi:10.1136/jech.55.1.38>. Low and Low (2004)
<doi:10.1093/pubmed/fdh175>.

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

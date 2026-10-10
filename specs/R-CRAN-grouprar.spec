%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grouprar
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Response Adaptive Randomization for Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-stats 
Requires:         R-CRAN-extraDistr 
Requires:         R-stats 

%description
Implements group response-adaptive randomization procedures, which include
standard (non-group) response-adaptive randomization methods as special
cases. The package also handles delayed and missing responses, which
broadens its use in real-world trials. It offers functions for simulating
a variety of response-adaptive randomization procedures, to help guide the
choice of design for a clinical trial, including the doubly adaptive
biased coin design and the multi-arm efficient randomized adaptive design
(ERADE), k-arm optimal target allocations, group sequential monitoring,
and a function that computes allocation probabilities for an ongoing
trial. For details of the methods and algorithms, see the following
references: Wei, L. J. (1979) <doi:10.1214/aos/1176344614>; Wei, L. J. and
Durham, S. (1978) <doi:10.1080/01621459.1978.10480109>; Durham, S. D.,
Flournoy, N. and Li, W. (1998) <doi:10.2307/3315771>; Ivanova, A.,
Rosenberger, W. F., Durham, S. D. and Flournoy, N. (2000)
<https://www.jstor.org/stable/25053121>; Bai, Z. D., Hu, F. and Shen, L.
(2002) <doi:10.1006/jmva.2001.1987>; Ivanova, A. (2003)
<doi:10.1007/s001840200220>; Hu, F. and Zhang, L. X. (2004)
<doi:10.1214/aos/1079120137>; Hu, F. and Rosenberger, W. F. (2006,
ISBN:978-0-471-65396-7); Zhang, L. X., Chan, W. S., Cheung, S. H. and Hu,
F. (2007) <https://www.jstor.org/stable/26432528>; Zhang, L. and
Rosenberger, W. F. (2006) <doi:10.1111/j.1541-0420.2005.00496.x>; Hu, F.,
Zhang, L. X., Cheung, S. H. and Chan, W. S. (2008)
<doi:10.1002/cjs.5550360404>; Tymofyeyev, Y., Rosenberger, W. F. and Hu,
F. (2007) <doi:10.1198/016214506000000906>; Hu, F., Zhang, L. X. and He,
X. (2009) <doi:10.1214/08-AOS655>; Zhu, H. and Hu, F. (2010)
<doi:10.1214/10-AOS796>; Zhai, G., Li, Y., Zhang, L. and Hu, F. (2024)
<doi:10.1002/sim.10220>; Alkhnefr, N., Hu, F. and Zhai, G. (2025)
<doi:10.1177/09622802251362644>.

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

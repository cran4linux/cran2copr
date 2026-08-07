%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UniIS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Importance Sampling Inference for Censored Univariate Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Distribution-independent framework for importance-sampling inference with
univariate observations subject to censoring or truncation. Users provide
probability functions and a proposal over model parameters. Constructs
observed-data likelihood contributions, computes numerically stable
importance weights, and supplies posterior, likelihood, predictive,
diagnostic, and model-comparison summaries. Covers complete, right, left,
interval, Type-I, Type-II, progressive Type-II, first-failure, progressive
first-failure, doubly Type-II, middle-censored, and left/right-truncated
data. Methods for importance sampling and censoring schemes are described
in Geweke (1989) <doi:10.2307/2290062>, Hesterberg (1995)
<doi:10.1080/00031305.1995.10476138>, Robert and Casella (2004,
ISBN:978-0-387-21617-1), Kundu and Joarder (2006)
<doi:10.1016/j.csda.2005.05.002>, Banerjee and Kundu (2008)
<doi:10.1109/TR.2008.916890>, Iyer, Jammalamadaka, and Kundu (2008)
<doi:10.1016/j.jspi.2007.03.062>, Wu and Kus (2009)
<doi:10.1016/j.csda.2009.03.010>, Prajapati, Mitra, and Kundu (2019)
<doi:10.1007/s13571-018-0167-0>, Mondal and Kundu (2020)
<doi:10.1080/03610926.2018.1554128>, Balakrishnan and Aggarwala (2000,
ISBN:980-1-4612-1334-5), Ding and Gui (2023) <doi:10.3390/math11092003>,
Nagar, Kumar, and Krishna (2026) <doi:10.59467/IJASS.2026.22.1>, Goel and
Krishna (2026) <doi:10.1007/s13198-026-03208-w>, Yadav, Jaiswal, and Yadav
(2026) <doi:10.1007/s11135-026-02647-8>, and Goel, Kumar, and Krishna
(2026, "Estimation in power Lindley distributions using balanced joint
progressively Type-II censored data").

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

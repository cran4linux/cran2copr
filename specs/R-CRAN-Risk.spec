%global __brp_check_rpaths %{nil}
%global packname  Risk
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Computes 26 Financial Risk Measures for Any ContinuousDistribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
Computes 26 financial risk measures for any continuous distribution.  The
26 financial risk measures include value at risk, expected shortfall due
to Artzner et al. (1999) <DOI:10.1007/s10957-011-9968-2>, tail conditional
median due to Kou et al. (2013) <DOI:10.1287/moor.1120.0577>, expectiles
due to Newey and Powell (1987) <DOI:10.2307/1911031>, beyond value at risk
due to Longin (2001) <DOI:10.3905/jod.2001.319161>, expected proportional
shortfall due to Belzunce et al. (2012)
<DOI:10.1016/j.insmatheco.2012.05.003>, elementary risk measure due to
Ahmadi-Javid (2012) <DOI:10.1007/s10957-011-9968-2>, omega due to Shadwick
and Keating (2002), sortino ratio due to Rollinger and Hoffman (2013),
kappa due to Kaplan and Knowles (2004), Wang (1998)'s
<DOI:10.1080/10920277.1998.10595708> risk measures, Stone (1973)'s
<DOI:10.2307/2978638> risk measures, Luce (1980)'s
<DOI:10.1007/BF00135033> risk measures, Sarin (1987)'s
<DOI:10.1007/BF00126387> risk measures, Bronshtein and Kurelenkova
(2009)'s risk measures.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

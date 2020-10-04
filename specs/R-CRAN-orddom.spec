%global packname  orddom
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Ordinal Dominance Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-psych 

%description
Computes ordinal, statistics and effect sizes as an alternative to mean
comparison: Cliff's delta or success rate difference (SRD), Vargha and
Delaney's A or the Area Under a Receiver Operating Characteristic Curve
(AUC), the discrete type of McGraw & Wong's Common Language Effect Size
(CLES) or Grissom & Kim's Probability of Superiority (PS), and the Number
needed to treat (NNT) effect size. Moreover, comparisons to Cohen's d are
offered based on Huberty & Lowman's Percentage of Group (Non-)Overlap
considerations.

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

%files
%{rlibdir}/%{packname}

%global __brp_check_rpaths %{nil}
%global packname  RankAggregator
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Aggregation of (Partial) Ordinal Rankings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Easily compute an aggregate ranking (also called a median ranking or a
consensus ranking) according to the axiomatic approach presented by Cook
et al. (2007). This approach minimises the number of violations between
all candidate consensus rankings and all input (partial) rankings, and
draws on a branch and bound algorithm and a heuristic algorithm to
drastically improve speed. The package also provides an option to
bootstrap a consensus ranking based on resampling input rankings (with
replacement). Input rankings can be either incomplete (partial) or
complete. Reference: Cook, W.D., Golany, B., Penn, M. and Raviv, T. (2007)
<doi:10.1016/j.cor.2005.05.030>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctreeMI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Inference Trees with Stacked Multiple Imputation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.0.0
BuildRequires:    R-CRAN-partykit >= 1.2.0
BuildRequires:    R-methods 
Requires:         R-CRAN-mice >= 3.0.0
Requires:         R-CRAN-partykit >= 1.2.0
Requires:         R-methods 

%description
Implements the stacked-imputation workflow for conditional inference trees
('ctree') described in Sherlock et al. (2026)
<doi:10.1080/00273171.2026.2661244>. When data contain missing values,
multiply imputed datasets (e.g., from 'mice') are stacked vertically and a
single 'ctree' is fit on the combined data. To correct for the
artificially inflated sample size introduced by stacking, the pruning
significance threshold is divided by the number of imputations M (the
Stack/M correction), producing a conservative but interpretable single
tree that incorporates imputation uncertainty without requiring pooling of
structurally different trees. Also exports stack_imputations() and
rescale_alpha() as standalone utilities. The underlying 'ctree' algorithm
is provided by 'partykit' (Hothorn & Zeileis, 2015; Hothorn, Hornik &
Zeileis, 2006 <doi:10.1198/106186006X133933>).

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

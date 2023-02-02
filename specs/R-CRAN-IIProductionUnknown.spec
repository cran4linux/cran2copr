%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IIProductionUnknown
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Data Through of Percentage of Importance Indice (Production Unknown) and Its Derivations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-crayon 

%description
The Importance Index (I.I.) can determine the loss and solution sources
for a system in certain knowledge areas (e.g., agronomy), when production
(e.g., fruits) is known (Demolin-Leite, 2021). Events (e.g., agricultural
pest) can have different magnitudes (numerical measurements), frequencies,
and distributions (aggregate, random, or regular) of event occurrence, and
I.I. bases in this triplet (Demolin-Leite, 2021)
<https://cjascience.com/index.php/CJAS/article/view/1009/1319>. Usually,
the higher the magnitude and frequency of aggregated distribution, the
greater the problem or the solution (e.g., natural enemies versus pests)
for the system (Demolin-Leite, 2021). However, the final production of the
system is not always known or is difficult to determine (e.g., degraded
area recovery). A derivation of the I.I. is the percentage of Importance
Index-Production Unknown (%% I.I.-PU) that can detect the loss or solution
sources, when production is unknown for the system (Demolin-Leite, 2024)
<DOI:10.1590/1519-6984.253218>.

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

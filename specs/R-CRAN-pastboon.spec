%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pastboon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Parameterized Stochastic Boolean Networks

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Applying stochastic noise to Boolean networks is a useful approach for
representing the effects of various perturbing stimuli on complex systems.
A number of methods have been developed to control noise effects on
Boolean networks using parameters integrated into the update rules. This
package provides functions to examine three such methods: BNp (Boolean
network with perturbations), described by Trairatphisan et al. (2013)
<doi:10.1186/1478-811X-11-46>, SDDS (stochastic discrete dynamical
systems), proposed by Murrugarra et al. (2012)
<doi:10.1186/1687-4153-2012-5>, and PEW (Boolean network with
probabilistic edge weights), presented by Deritei et al. (2022)
<doi:10.1371/journal.pcbi.1010536>. This package includes source code
derived from the 'BoolNet' package, which is licensed under the Artistic
License 2.0.

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

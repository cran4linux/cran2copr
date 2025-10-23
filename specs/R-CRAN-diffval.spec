%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diffval
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vegetation Patterns

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 

%description
Find, visualize and explore patterns of differential taxa in vegetation
data (namely in a phytosociological table), using the Differential Value
(DiffVal). Patterns are searched through mathematical optimization
algorithms. Ultimately, Total Differential Value (TDV) optimization aims
at obtaining classifications of vegetation data based on differential
taxa, as in the traditional geobotanical approach (Monteiro-Henriques
2025, <doi:10.3897/VCS.140466>). The Gurobi optimizer, as well as the R
package 'gurobi', can be installed from
<https://www.gurobi.com/products/gurobi-optimizer/>.  The useful vignette
Gurobi Installation Guide, from package 'prioritizr', can be found here:
<https://prioritizr.net/articles/gurobi_installation_guide.html>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smallsets
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visual Documentation for Data Preprocessing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rmarkdown 

%description
Data practitioners regularly use the 'R' and 'Python' programming
languages to prepare data for analyses. Thus, they encode important data
preprocessing decisions in 'R' and 'Python' code. The 'smallsets' package
subsequently decodes these decisions into a Smallset Timeline, a static,
compact visualisation of data preprocessing decisions (Lucchesi et al.
(2022) <doi:10.1145/3531146.3533175>). The visualisation consists of small
data snapshots of different preprocessing steps. The 'smallsets' package
builds this visualisation from a user's dataset and preprocessing code
located in an 'R', 'R Markdown', 'Python', or 'Jupyter Notebook' file.
Users simply add structured comments with snapshot instructions to the
preprocessing code. One optional feature in 'smallsets' requires
installation of the 'Gurobi' optimisation software and 'gurobi' 'R'
package, available from <https://www.gurobi.com>. More information
regarding the optional feature and 'gurobi' installation can be found in
the 'smallsets' vignette.

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

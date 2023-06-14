%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcutils
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Some Useful Functions for Statistics and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-agricolae 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-agricolae 

%description
Offers a range of utilities and functions for everyday programming tasks.
1.Data Manipulation. Such as grouping and merging, column splitting, and
character expansion. 2.File Handling. Read and convert files in popular
formats, including "blast", "diamond", "fasta", "gff", "gtf", and various
image formats like "jpg", "png", "pdf", and "svg". 3.Plotting Assistance.
Helpful utilities for generating color palettes, validating color formats,
and adding transparency. 4.Statistical Analysis. Includes functions for
pairwise comparisons and multiple testing corrections, enabling perform
statistical analyses with ease. 5.Graph Plotting, Provides efficient tools
for creating doughnut plot and multi-layered doughnut plot; Venn diagrams,
including traditional Venn diagrams, upset plots, and flower plots;
Simplified functions for creating stacked bar plots, or a box plot with
alphabets group for multiple comparison group.

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

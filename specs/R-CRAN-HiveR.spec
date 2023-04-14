%global __brp_check_rpaths %{nil}
%global packname  HiveR
%global packver   0.3.63
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.63
Release:          3%{?dist}%{?buildtag}
Summary:          2D and 3D Hive Plots for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-tcltk 
Requires:         R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rgl 
Requires:         R-tcltk 

%description
Creates and plots 2D and 3D hive plots. Hive plots are a unique method of
displaying networks of many types in which node properties are mapped to
axes using meaningful properties rather than being arbitrarily positioned.
The hive plot concept was invented by Martin Krzywinski at the Genome
Science Center (www.hiveplot.net/).  Keywords: networks, food webs,
linnet, systems biology, bioinformatics.

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

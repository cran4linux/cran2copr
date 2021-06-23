%global __brp_check_rpaths %{nil}
%global packname  ggdendro
%global packver   0.1.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.22
Release:          1%{?dist}%{?buildtag}
Summary:          Create Dendrograms and Tree Diagrams Using 'ggplot2'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-MASS 
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-MASS 

%description
This is a set of tools for dendrograms and tree plots using 'ggplot2'.
The 'ggplot2' philosophy is to clearly separate data from the
presentation. Unfortunately the plot method for dendrograms plots directly
to a plot device without exposing the data. The 'ggdendro' package
resolves this by making available functions that extract the dendrogram
plot data. The package provides implementations for 'tree', 'rpart', as
well as diana and agnes (from 'cluster') diagrams.

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

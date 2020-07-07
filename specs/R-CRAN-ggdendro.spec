%global packname  ggdendro
%global packver   0.1-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.20
Release:          3%{?dist}
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
plot data. The package provides implementations for tree, rpart, as well
as diana and agnes cluster diagrams.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX

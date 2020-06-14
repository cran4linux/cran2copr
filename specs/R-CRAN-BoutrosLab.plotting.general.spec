%global packname  BoutrosLab.plotting.general
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          2%{?dist}
Summary:          Functions to Create Publication-Quality Plots

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-MASS >= 7.3.29
BuildRequires:    R-CRAN-hexbin >= 1.26.3
BuildRequires:    R-cluster >= 1.14.4
BuildRequires:    R-CRAN-latticeExtra >= 0.6.26
BuildRequires:    R-lattice >= 0.20.27
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-e1071 
Requires:         R-MASS >= 7.3.29
Requires:         R-CRAN-hexbin >= 1.26.3
Requires:         R-cluster >= 1.14.4
Requires:         R-CRAN-latticeExtra >= 0.6.26
Requires:         R-lattice >= 0.20.27
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-tools 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-e1071 

%description
Contains several plotting functions such as barplots, scatterplots,
heatmaps, as well as functions to combine plots and assist in the creation
of these plots. These functions will give users great ease of use and
customization options in broad use for biomedical applications, as well as
general purpose plotting. Each of the functions also provides valid
default settings to make plotting data more efficient and producing high
quality plots with standard colour schemes simpler. All functions within
this package are capable of producing plots that are of the quality to be
presented in scientific publications and journals.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ext2function.txt
%doc %{rlibdir}/%{packname}/optimal.heatmap.cex.txt
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  SDMPlay
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Species Distribution Modelling Playground

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-stats 
BuildRequires:    R-base 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-SDMTools 
Requires:         R-CRAN-gbm 
Requires:         R-stats 
Requires:         R-base 

%description
Functions provided by this pedagogic package allow to compute models with
two popular machine learning approaches, BRT (Boosted Regression Trees)
and MaxEnt (Maximum Entropy) applied on sets of marine biological and
environmental data. They include the possibility of managing the main
parameters for the construction of the models. Classic tools to evaluate
model performance are provided (Area Under the Curve, omission rate and
confusion matrix, map standard deviation) and are completed with tools to
perform null models. The biological dataset includes original occurrences
of two species of the class Echinoidea (sea urchins) present on the
Kerguelen Plateau and that show contrasted ecological niches. The
environmental dataset includes the corresponding statistics for 15 abiotic
and biotic descriptors summarized for the Kerguelen Plateau and for
different periods in a raster format. The package can be used for
practicals to teach and learn the basics of species distribution
modelling. Maps of potential distribution can be produced based on the
example data included in the package, which brings prior observations of
the influence of spatial and temporal heterogeneities on modelling
performances. The user can also provide his own datasets to use the
modelling functions.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/vignette_data
%{rlibdir}/%{packname}/INDEX

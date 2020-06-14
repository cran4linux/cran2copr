%global packname  ModelMap
%global packver   3.4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0.1
Release:          2%{?dist}
Summary:          Modeling and Map Production using Random Forest and RelatedStochastic Models

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-HandTill2001 
BuildRequires:    R-CRAN-PresenceAbsence 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-mgcv 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-HandTill2001 
Requires:         R-CRAN-PresenceAbsence 

%description
Creates sophisticated models of training data and validates the models
with an independent test set, cross validation, or Out Of Bag (OOB)
predictions on the training data. Create graphs and tables of the model
validation results. Applies these models to GIS .img files of predictors
to create detailed prediction surfaces. Handles large predictor files for
map making, by reading in the .img files in chunks, and output to the .txt
file the prediction for each data chunk, before reading the next chunk of
data.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX

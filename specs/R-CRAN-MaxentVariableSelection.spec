%global packname  MaxentVariableSelection
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Selecting the Best Set of Relevant Environmental Variables alongwith the Optimal Regularization Multiplier for Maxent NicheModeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-raster 

%description
Complex niche models show low performance in identifying the most
important range-limiting environmental variables and in transferring
habitat suitability to novel environmental conditions (Warren and Seifert,
2011 <DOI:10.1890/10-1171.1>; Warren et al., 2014
<DOI:10.1111/ddi.12160>). This package helps to identify the most
important set of uncorrelated variables and to fine-tune Maxent's
regularization multiplier. In combination, this allows to constrain
complexity and increase performance of Maxent niche models (assessed by
information criteria, such as AICc (Akaike, 1974
<DOI:10.1109/TAC.1974.1100705>), and by the area under the receiver
operating characteristic (AUC) (Fielding and Bell, 1997
<DOI:10.1017/S0376892997000088>). Users of this package should be familiar
with Maxent niche modelling.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

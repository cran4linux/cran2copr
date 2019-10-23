%global packname  texteffect
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Discovering Latent Treatments in Text Corpora and EstimatingTheir Causal Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-CRAN-ggplot2 

%description
Implements the approach described in Fong and Grimmer (2016)
<https://aclweb.org/anthology/P/P16/P16-1151.pdf> for automatically
discovering latent treatments from a corpus and estimating the average
marginal component effect (AMCE) of each treatment.  The data is divided
into a training and test set.  The supervised Indian Buffet Process (sibp)
is used to discover latent treatments in the training set.  The fitted
model is then applied to the test set to infer the values of the latent
treatments in the test set.  Finally, Y is regressed on the latent
treatments in the test set to estimate the causal effect of each
treatment.

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
%{rlibdir}/%{packname}/INDEX

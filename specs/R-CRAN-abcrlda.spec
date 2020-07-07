%global packname  abcrlda
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Asymptotically Bias-Corrected Regularized Linear DiscriminantAnalysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Offers methods to perform asymptotically bias-corrected regularized linear
discriminant analysis (ABC_RLDA) for cost-sensitive binary classification.
The bias-correction is an estimate of the bias term added to regularized
discriminant analysis (RLDA) that minimizes the overall risk. The default
magnitude of misclassification costs are equal and set to 0.5; however,
the package also offers the options to set them to some predetermined
values or, alternatively, take them as hyperparameters to tune. A.
Zollanvari, M. Abdirash, A. Dadlani and B. Abibullaev (2019)
<doi:10.1109/LSP.2019.2918485>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/abcrlda_1.0.3.pdf
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global packname  rasclass
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Supervised Raster Image Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-RSNNS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-nnet 
Requires:         R-CRAN-RSNNS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 

%description
Software to perform supervised and pixel based raster image
classification. It has been designed to facilitate land-cover analysis.
Five classification algorithms can be used: Maximum Likelihood
Classification, Multinomial Logistic Regression, Neural Networks, Random
Forests and Support Vector Machines. The output includes the classified
raster and standard classification accuracy assessment such as the
accuracy matrix, the overall accuracy and the kappa coefficient. An option
for in-sample verification is available.

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

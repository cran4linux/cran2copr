%global __brp_check_rpaths %{nil}
%global packname  rocsvm.path
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Entire Solution Paths for ROC-SVM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-svmpath 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-svmpath 

%description
We develop the entire solution paths for ROC-SVM presented by
Rakotomamonjy. The ROC-SVM solution path algorithm greatly facilitates the
tuning procedure for regularization parameter, lambda in ROC-SVM by
avoiding grid search algorithm which may be computationally too intensive.
For more information on the ROC-SVM, see the report in the ROC Analysis in
AI workshop(ROCAI-2004) : Hernàndez-Orallo, José, et al. (2004)
<doi:10.1145/1046456.1046489>.

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

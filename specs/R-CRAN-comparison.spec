%global __brp_check_rpaths %{nil}
%global packname  comparison
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Likelihood Ratio Calculation and Evaluation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-isotone 
Requires:         R-CRAN-isotone 

%description
Functions for calculating and evaluating likelihood ratios from
uni/multivariate continuous observations. The package includes the
two-level functions to calculate the LR assuming multivariate normality,
and another with drops this assumption and uses a multivariate kernel
density estimate. The package also contains code to perform empirical
cross entropy (ECE) calibration of likelihood ratios. The LR functions are
based primarily on Aitken, C.G.G. and Lucy, D. (2004)
<doi:10.1046/j.0035-9254.2003.05271.x>, "Evaluation of trace evidence in
the form of multivariate data," Journal of the Royal Statistical Society:
Series C (Applied Statistics), 53: 109-122. The ECE functions are based
primarily on D. Ramos and J. Gonzalez-Rodrigues, (2008) "Cross-entropy
analysis of the information in forensic speaker recognition," in Proc.
IEEE Odyssey, Speaker Lang. Recognit. Workshop.

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

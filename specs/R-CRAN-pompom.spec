%global packname  pompom
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Person-Oriented Method and Perturbation on the Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-lavaan >= 0.5.23.1097
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-lavaan >= 0.5.23.1097
Requires:         R-CRAN-qgraph 
Requires:         R-utils 

%description
An implementation of a hybrid method of person-oriented method and
perturbation on the model. Pompom is the initials of the two methods. The
hybrid method will provide a multivariate intraindividual variability
metric (iRAM). The person-oriented method used in this package refers to
uSEM (unified structural equation modeling, see Kim et al., 2007, Gates et
al., 2010 and Gates et al., 2012 for details). Perturbation on the model
was conducted according to impulse response analysis introduced in
Lutkepohl (2007). Kim, J., Zhu, W., Chang, L., Bentler, P. M., & Ernst, T.
(2007) <doi:10.1002/hbm.20259>. Gates, K. M., Molenaar, P. C. M., Hillary,
F. G., Ram, N., & Rovine, M. J. (2010)
<doi:10.1016/j.neuroimage.2009.12.117>. Gates, K. M., & Molenaar, P. C. M.
(2012) <doi:10.1016/j.neuroimage.2012.06.026>. Lutkepohl, H. (2007,
ISBN:3540262393).

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

%files
%{rlibdir}/%{packname}

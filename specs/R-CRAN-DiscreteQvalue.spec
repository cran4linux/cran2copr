%global packname  DiscreteQvalue
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Improved q-Values for Discrete Uniform and Homogeneous Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
We consider a multiple testing procedure used in many modern applications
which is the q-value method proposed by Storey and Tibshirani (2003),
<doi:10.1073/pnas.1530509100>. The q-value method is based on the false
discovery rate (FDR), hence versions of the q-value method can be defined
depending on which estimator of the proportion of true null hypotheses,
p0, is plugged in the FDR estimator. We implement the q-value method based
on two classical pi0 estimators, and furthermore, we propose and implement
three versions of the q-value method for homogeneous discrete uniform
P-values based on pi0 estimators which take into account the discrete
distribution of the P-values.

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
%{rlibdir}/%{packname}/INDEX

%global packname  bestNormalize
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          Normalizing Transformation Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LambertW 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-CRAN-LambertW 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 

%description
Estimate a suite of normalizing transformations, including a new
adaptation of a technique based on ranks which can guarantee normally
distributed transformed data if there are no ties: ordered quantile
normalization (ORQ). ORQ normalization combines a rank-mapping approach
with a shifted logit approximation that allows the transformation to work
on data outside the original domain. It is also able to handle new data
within the original domain via linear interpolation. The package is built
to estimate the best normalizing transformation for a vector consistently
and accurately. It implements the Box-Cox transformation, the Yeo-Johnson
transformation, three types of Lambert WxF transformations, and the
ordered quantile normalization transformation. It also estimates the
normalization efficacy of other commonly used transformations.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

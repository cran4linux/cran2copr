%global packname  sparsestep
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          SparseStep Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.0.6
BuildRequires:    R-graphics 
Requires:         R-Matrix >= 1.0.6
Requires:         R-graphics 

%description
Implements the SparseStep model for solving regression problems with a
sparsity constraint on the parameters. The SparseStep regression model was
proposed in Van den Burg, Groenen, and Alfons (2017)
<https://arxiv.org/abs/1701.06967>. In the model, a regularization term is
added to the regression problem which approximates the counting norm of
the parameters.  By iteratively improving the approximation a sparse
solution to the regression problem can be obtained.  In this package both
the standard SparseStep algorithm is implemented as well as a path
algorithm which uses golden section search to determine solutions with
different values for the regularization parameter.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

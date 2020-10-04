%global packname  polyMatrix
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Infrastructure for Manipulation Polynomial Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-polynom 
Requires:         R-stats 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-polynom 

%description
Implementation of class "polyMatrix" for storing a matrix of polynomials
and implements basic matrix operations; including a determinant and
characteristic polynomial. It is based on the package 'polynom' and uses a
lot of its methods to implement matrix operations. This package includes 3
methods of triangularization of polynomial matrices: Extended Euclidean
algorithm which is most classical but numerically unstable; Sylvester
algorithm based on LQ decomposition; Interpolation algorithm is based on
LQ decomposition and Newton interpolation. Both methods are described in
D. Henrion & M. Sebek, Reliable numerical methods for polynomial matrix
triangularization, IEEE Transactions on Automatic Control (Volume 44,
Issue 3, Mar 1999, Pages 497-508) <doi:10.1109/9.751344> and in Salah
Labhalla, Henri Lombardi & Roger Marlin, Algorithmes de calcule de la
reduction de Hermite d'une matrice a coefficients polynomeaux, Theoretical
Computer Science (Volume 161, Issue 1-2, July 1996, Pages 69-92)
<doi:10.1016/0304-3975(95)00090-9>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

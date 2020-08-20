%global packname  hiphop
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parentage Assignment using Bi-Allelic Genetic Markers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch

%description
Can be used for paternity and maternity assignment and outperforms
conventional methods where closely related individuals occur in the pool
of possible parents. The method compares the genotypes of offspring with
any combination of potentials parents and scores the number of mismatches
of these individuals at bi-allelic genetic markers (e.g. Single Nucleotide
Polymorphisms). It elaborates on a prior exclusion method based on the
Homozygous Opposite Test (HOT; Huisman 2017 <doi:10.1111/1755-0998.12665>)
by introducing the additional exclusion criterion HIPHOP (Homozygous
Identical Parents, Heterozygous Offspring are Precluded; Cockburn et al.,
in revision). Potential parents are excluded if they have more mismatches
than can be expected due to genotyping error and mutation, and thereby one
can identify the true genetic parents and detect situations where one (or
both) of the true parents is not sampled. Package 'hiphop' can deal with
(a) the case where there is contextual information about parentage of the
mother (i.e. a female has been seen to be involved in reproductive tasks
such as nest building), but paternity is unknown (e.g. due to
promiscuity), (b) where both parents need to be assigned, because there is
no contextual information on which female laid eggs and which male
fertilized them (e.g. polygynandrous mating system where multiple females
and males deposit young in a common nest, or organisms with external
fertilisation that breed in aggregations). For details: Cockburn, A.,
Penalba, J.V.,Jaccoud, D.,Kilian, A., Brouwer, L., Double, M.C., Margraf,
N., Osmond, H.L., van de Pol, M. and Kruuk, L.E.B. (in revision). HIPHOP:
improved paternity assignment among close relatives using a simple
exclusion method for bi-allelic markers. Molecular Ecology Resources, DOI
to be added upon acceptance.

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
